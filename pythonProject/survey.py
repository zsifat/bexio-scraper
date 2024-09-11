class AnonymousSurvey:
	"""Collect anonymous answers to a survey question."""

	def __init__(self,question):
		self.question=question
		self.responses=[]

	def show_question(self):
		print(self.question)

	def store_respones(self,new_response):
		self.responses.append(new_response)

	def show_result(self):
		print("Survey Results are:")
		for response in self.responses:
			print(f'\t-{response}')

	def analysis_response(self):
		i=0
		j=0
		k=0
		for response in self.responses:
			response=int(response)
			if response>=18:
				i+=1
			elif response>=10 and response<18:
				j+=1
			elif response<10:
				k+=1
		print(f'Adult person: {i}')
		print(f'Teen person: {j}')
		print(f'Child person: {k}')

survey=AnonymousSurvey('Age')
while True:
	survey.show_question()
	response=input('Your age= ')
	if response.lower()=='q':
		break
	else:
		survey.store_respones(response)

survey.show_result()
survey.analysis_response()


