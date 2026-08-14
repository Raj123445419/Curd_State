from django.db import models

# Create your models here.



class Country(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='state')
    name = models.CharField(max_length=100)



    def __str__(self):
        return f"{self.name} ({self.country.name})"



class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')
    name = models.CharField(max_length=100)



    def __str__(self):
        return f"{self.name} ({self.state.name})"
    
class userSelation(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    City = models.ForeignKey(City, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.country.name} -> {self.state.name} -> {self.City.name}"






