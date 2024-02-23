from utils.human import Human

def main():
     
    john = Human(name='John Doe', age=24, gender='M', height_in_inches=75)
    john.weight_setter(125)
    print(john.get_first_name())
    print('----')
    print(john.get_last_name())
    
    
    
   
    

if __name__ == '__main__':
    main()