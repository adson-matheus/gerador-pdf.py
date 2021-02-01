import requests
from reportlab.pdfgen import canvas
#a página possui 595.27 de largura e 841.89 de altura no padrão A4
#programa para gerar pdf a partir de dados de uma api

def pdfGenerator(cidades, ddd, state):
	try:
		nome_pdf = input('Nome do pdf: ')
		pdf = canvas.Canvas('%s.pdf'%nome_pdf)
		y = 800
		for i in cidades:
			pdf.drawString(245,y, '%s'%i)
			y -= 20
		pdf.setTitle('Cidades do %s'%state)
		pdf.drawString(245,820, 'Lista de cidades - %s'%state)
		pdf.save()
		print('%s.pdf criado com sucesso'%nome_pdf)
	except:
		print('erro ao gerar pdf.')

def main():
	print('Gerador de pdf das cidades!\n')
	url = 'https://brasilapi.com.br/api/ddd/v1/'
	ddd = input('ddd do estado: ')

	#faz o request e retorna em .json
	consulta = requests.get('%s%s' %(url, ddd)).json()
	
	state = consulta['state']
	cidades = consulta['cities']
	pdfGenerator(cidades, ddd, state)

if __name__ == '__main__':
	main()