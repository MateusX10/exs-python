from math import sin, cos, tan, radians
ang = float(input("Digite um ângulo: "))
print(f'O \033[1;32mSENO\033[m de {ang}º é {sin(radians(ang)):.2f} \nO \033[1;32mCOSSENO\033[m de {ang}º é {cos(radians(ang)):.2f} \nA \033[1;32mTANGENTE\033[m de {ang}º é {tan(radians(ang)):.2f} ')
