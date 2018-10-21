# Exercises list and solutions

All the exercises are in the same order as the presentation, even if numbering is not the same.

1. Obter o 2º, 3º e 4º caracteres  da string "Anatomia".

```python
str = 'Anatomia'
print(str[1])
print(str[2])
print(str[3])
```

2. Concatenar as strings 'ester', 'no', 'cleido', 'mas', 'toideu' e indicar o tamanho da string final.

```python
print(len('ester'+'no'+'cleido'+'mas'+'toideu'))
```

3. Comparar as palavras 'casa' e 'Casa', com <, > e ==.

```python
print('casa' < 'Casa')
print('casa' > 'Casa')
print('casa' == 'Casa')
```

4. Ler uma string da consola e apresentar o seu tamanho formatado na string: "A minha string tem xx letras".

```python
str = input('Insira uma string: ')
print('A minha string tem {} letras'.format(len(str)))
```

5. Verificar se a palavra biomédica está presente no seguinte texto : "A Engenharia biomédica é uma área que integra princípios das ciências exatas e ciências da saúde."

```python
str = "A Engenharia biomédica é uma área que integra princípios das ciências exatas e ciências da saúde."
print('biomédica' in str)
```

6. Ler altura e peso da consola e calcular IMC com o valor formatado. IMC = altura / massa² (m/kg²)

```python
altura = float(input('Insira a altura: '))
massa = float(input('Insira a massa: '))
imc = altura / massa ** 2
print(imc)
```

7. Listar o valor lógico da inclusão do IMC nas categorias seguintes:
[17   ; 18,5[ - Magreza leve: True or False?
[18,5 ; 25  [ - Saudável: True or False?
[25   ; 30  [ - Sobrepeso: True or False?

```python
print('Magreza leve: '+str(imc >= 17 and imc < 18.5))
print('Saudável: '+str(imc >= 18.5 and imc < 25))
print('Sobrepeso: '+str(imc >= 25 and imc < 30))
```

8. Ler IMC da consola e escrever uma mensagem consoante o intervalo do IMC

```python
imc = input('O seu imc: ')
if imc >= 17 and imc < 18.5:
	print('Magreza leve')
elif imc >= 18.5 and imc < 25:
	print('Saudável')
elif imc >= 25 and imc < 30:
	print('Sobrepeso')
else: 
	print('Fora da escala!!')
```
 
9. Ler lista de valores de valores de IMC e achar o max e min: 
	lista de IMCs: [12, 17.5, 22, 26, 15.4]

```python
imcs = [12, 17.5, 22, 26, 15.4]
print('Min: '+str(min(imcs)))
print('Max: '+str(max(imcs)))
```

10. Ordenar a lista anterior por ordem crescente

```python
imcs = [12, 17.5, 22, 26, 15.4]
sorted_imcs = sorted(imcs)
print(sorted_imcs)

# Outra opcao
imcs = [12, 17.5, 22, 26, 15.4]
imcs.sort()
print(imcs)
```

11. Criar dicionario com nome paciente, altura e peso, e calcular o IMC desse paciente

```python
paciente = {
	'nome': 'ricardo', 
	'peso': 80, # Kg
	'altura': 1.80 # metros
}
imc = paciente['altura'] / paciente['peso']**2
print(imc)
```

12. Repetir o exercicio anterior mas usando tuples

```python
paciente = ('ricardo', 80, 1.80)
imc = paciente[2] / paciente[1]**2
print(imc)
```
 
13. Criar uma lista de números naturais ímpares até 50

```python
nums = []
for i in range(1,51):
	if i % 2 != 0:
		nums.append(i)
print(nums)

# outra forma
nums = [i for i in range(1,51) if i%2!=0]
print(nums)
```

14. Multiplicar cada elemento da lista [1, 2, 3] por 3 e colocar numa nova variável.

```python
list = [1,2,3]
multiplied = [item*3 for item in list] 
print(multiplied)
```

15. Criar uma lista da primeira letra de cada palabra do vector: words = ["this","is","a","list","of","words"]

```python
words = ["this","is","a","list","of","words"]
items = [ word[0] for word in words ]
print(items)
```

16. Verificar se o n.º 10 existe no dicionário e indicar a sua chave: d = {'a':1, 'b':11, 'c':53, 'd':10, 'e':7}

```python
d = {'a':1, 'b':11, 'c':53, 'd':10, 'e':7}
print(10 in d.values())
keys = [k for (k, v) in d.items() if v == 10]
```

17. Converter todos os caracteres da lista para minúsculas. l = ['M', 'I', 'N', 'U', 'S', 'C', 'U', 'L', 'A', 'S']

```python
l = ['M', 'I', 'N', 'U', 'S', 'C', 'U', 'L', 'A', 'S']
ll = [c.lower() for c in l]
```

18. Criar função para calcular o IMC

```python
def imc(height, weight):
	return weight / height ** 2
```

19. Criar função para calcular calorias semanais com base na idade.
cal = [(20, 1200), (25, 1800), (30, 1600), (40, 1300)]

```python
def weekly_cal(age):
	cal = [(20, 1200), (25, 1800), (30, 1600), (40, 1300)]
	age_cal = [calv for (agev,calv) in cal if agev == age][0]
	return age_cal*7
```

20. Criar função para verificar existência de diabetes com base nos níveis de glicose no sangue

```python
def check_diabetes(patient):
    glucose = float(patient['glucose'])
    
    if glucose < 70:
        print('-> Está com hipoglicemia.')
    elif glucose >= 70 and glucose < 100:
        print('-> Está normal.')
    elif glucose >= 100 and glucose < 126:
        print('-> Está com pré-diabetes!')
    else:
        print('-> Está com diabetes!!!')
```