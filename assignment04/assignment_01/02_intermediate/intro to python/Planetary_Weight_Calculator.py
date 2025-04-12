def main():
    print("\033[1m🚀Intergalactic Weight Watcher!\033[0m")
    print("Have you ever wondered what you’d weigh if you were a space tourist? Let the planets judge you")
    earth_weight=int(input('Enter your weight on earth in kg: '))#user input
    print("Choose any:mercury, venus, mars, jupiter, saturn, uranus, neptune")
    planet_input=str(input('Enter a planet name: '))#user input planet
    #weight on mercury
    if planet_input == 'mercury':
      weight=earth_weight*0.376
      weight=round(weight,2)
    #weight on venus
    elif planet_input=='venus':
      weight=earth_weight*0.889
      weight=round(weight,2)
    #weight on mars
    elif planet_input=='mars':
      weight=earth_weight*0.378#calculating mars weight
      weight=round(weight,2)#rounding the weight to 2 decimal places
    #weight on jupiter
    elif planet_input=='jupiter':
      weight=earth_weight*0.236
      weight=round(weight,2)
    #weight on saturn
    elif planet_input=='saturn':
      weight=earth_weight*0.1081
      weight=round(weight,2)
    #weight on uranus
    elif planet_input=='uranus':
      weight=earth_weight*0.815
      weight=round(weight,2) 
    #weight on neptune
    elif planet_input=='neptune':
      weight=earth_weight*0.114
      weight=round(weight,2)
    else:
      print("Invalid request")#invalid input
   
    print(f"Your weight on {planet_input} is: {weight}")#response

if __name__ == '__main__':
  main()