# Exercises list and solutions

1. Ler altura e peso da consola e calcular IMC com o valor formatado. IMC = altura / massa² (m/kg²)

```python
altura = float(input('Insira a altura: '))
massa = float(input('Insira a massa: '))
imc = altura / massa ** 2
print(imc)
```

2. Listar o valor lógico da inclusão do IMC nas categorias seguintes:
[17   ; 18,5[ - Magreza leve: True or False?
[18,5 ; 25  [ - Saudável: True or False?
[25   ; 30  [ - Sobrepeso: True or False?

```python
print('Magreza leve: '+str(imc >= 17 and imc < 18.5))
print('Saudável: '+str(imc >= 18.5 and imc < 25))
print('Sobrepeso: '+str(imc >= 25 and imc < 30))
```

3. Ler IMC da consola e escrever uma mensagem consoante o intervalo do IMC

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
 
4. Ler lista de valores de valores de IMC e achar o max e min: 
	lista de IMCs: [12, 17.5, 22, 26, 15.4]

```python
imcs = [12, 17.5, 22, 26, 15.4]
print('Min: '+str(min(imcs)))
print('Max: '+str(max(imcs)))
```

5. Ordenar a lista anterior por ordem crescente

```python
imcs = [12, 17.5, 22, 26, 15.4]
sorted_imcs = sorted(imcs)
print(sorted_imcs)

# Outra opcao
imcs = [12, 17.5, 22, 26, 15.4]
imcs.sort()
print(imcs)
```

6. Criar dicionario com nome paciente, altura e peso, e calcular o IMC desse paciente

```python
paciente = {
	'nome': 'ricardo', 
	'peso': 80, # Kg
	'altura': 1.80 # metros
}
imc = paciente['altura'] / paciente['peso']**2
print(imc)
```

7. Repetir o exercicio anterior mas usando tuples

```python
paciente = ('ricardo', 80, 1.80)
imc = paciente[2] / paciente[1]**2
print(imc)
```
 
8. Criar uma lista de números naturais ímpares até 50

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

9. Criar função para calcular o IMC

```python
def imc(height, weight):
	return weight / height ** 2
```

10. Criar função para calcular calorias semanais com base na idade.
cal = [(20, 1200), (25, 1800), (30, 1600), (40, 1300)]

```python
def weekly_cal(age):
	cal = [(20, 1200), (25, 1800), (30, 1600), (40, 1300)]
	age_cal = [calv for (agev,calv) in cal if agev == age][0]
	return age_cal*7
```

11. Criar função para verificar existência de diabetes com base nos níveis de glicose no sangue

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