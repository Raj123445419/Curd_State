from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Curd_State_App.models import City, Country, State, userSelation
from Curd_State_App.serializers import CitySerializer, CountrySerializer, StateSerializer

# Create your views here.





class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']




class StateListView(generics.ListAPIView):
    serializer_class = StateSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


    def get_queryset(self):
        queryset = State.objects.all()
        country_id = self.request.query_params.get('country')

        if country_id:
            queryset = queryset.filter(country_id=country_id)


        return queryset


class CityListView(generics.ListAPIView):
    serializer_class = CitySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


    def get_queryset(self):
        queryset = City.objects.all()
        state_id = self.request.query_params.get('state')


        if state_id:
            queryset = queryset.filter(state_id=state_id)

        return queryset




class SubmitListView(generics.ListAPIView):
    def post(self, request):
        country_id = request.data.get('country')
        state_id = request.data.get('state')
        city_id = request.data.get('city')
        
        print(f"Received Data -> Country: {country_id}, State: {state_id}, City: {city_id}")
        
        # Check karein ki teeno IDs aayi hain ya nahi
        if not country_id or not state_id or not city_id:
            return Response({"error": "All fields (country, state, city) are required!"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Database mein save karein
            userSelation.objects.create(
                country_id=country_id,
                state_id=state_id,
                City_id=city_id  # Aapke model mein field ka naam 'City' (capital C) hai
            )
            
            return Response({"message": "Data successfully saved to database!"}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            print(f"Database Error: {str(e)}")  # Yeh terminal mein exact error dikhayega
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)