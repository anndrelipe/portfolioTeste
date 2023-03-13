
declare_cpf = input('Digite seu cpf:') #COLETAR
novocpf = (declare_cpf[:11].replace('.', '')) # Pegar os 9 primeiros dígitos.
conferircpf = (declare_cpf[:14].replace('.',''))
conferircpf2 = conferircpf.replace('-','')

contagem_reg = 10
resultado = 0

for digito in novocpf:
        resultado += int(digito) * contagem_reg
        contagem_reg -= 1

digito = (resultado * 10)
primeiro_digito = digito % 11
primeiro_digito == primeiro_digito if primeiro_digito <= 9 else primeiro_digito == 0
    
contagem_reg_segdigito = 11
resultado_segdigito = 0

novocpf += str(primeiro_digito)

for digito2 in novocpf:
        resultado_segdigito += int(digito2) * contagem_reg_segdigito
        contagem_reg_segdigito -= 1

resultado_segdigito = resultado_segdigito * 10
seg_digito = resultado_segdigito % 11
seg_digito == seg_digito if seg_digito <= 9 else seg_digito == 0
 

cpf = novocpf + str(seg_digito)

if cpf == conferircpf2:
        print(f'{cpf} é um CPF válido.')
else:
        print(f'{cpf} é um CPF inválido.')
