try:
  chats =['spicy_chat' , 'normal_chat' , 'chana_chat']
  dinner = ['biryani' , 'chicken' , 'beef' ,'mutton' ]
  sweet = ['ice_cream' , " cake" , 'custard']
  dish = input("Enter the dish name: ")

  if dish in chats:
    print(f'{dish} is in chats section' )
  elif dish in dinner:
    print(f'{dish} is in dinner section' )
  elif dish in sweet:
    print(f'{dish} is in sweet section' )

  else:
    print(f'{dish} is not present in any section')

except:
    print("invalid input")


