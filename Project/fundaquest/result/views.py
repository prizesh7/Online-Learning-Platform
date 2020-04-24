from django.shortcuts import render
from subjects.models import Subject
from exam.models import Question
from django.contrib import messages
import random
import ast



# Create your views here.
def take(request):
	if request.method=='GET':
		name = request.GET.get('name')
		print(name)
		if not name:
			return render(request, 'result/exam_test.html')
		else:
			s=Subject.objects.filter(subject_name=name)
			question=Question.objects.filter(subject__in=s).values()
			questions = list(question)
			five_list=[]
			while len(five_list) < 5:
				temp=random.choice(questions)
				if temp not in five_list:
					five_list.append(temp)
			print(five_list)
			if not questions:
				print("hello")
				messages.add_message(request,messages.WARNING,'no questions available')
				return render(request, 'result/exam_test.html')
			else:
				print("genk")
				return render(request, 'result/exam_test.html',{'questions':five_list})
			return render(request,'users/tregister.html',{})

def verify(request):
	if request.method=='POST':
		alll=request.POST.get('obj')
		res = ast.literal_eval(alll)
		l=[]
		for que in range(1,6):
			l1=[]
			id=request.POST.get('number' + str(que))
			l1.append(id)
			val=request.POST.get('radio'+id)
			l1.append(val)
			l.append(l1)
		print(l)
		count=0
		ans=0
		for i in range(0,5):
			temp=res[i]
			ansc=temp['answer']
			id=temp['question_id']
			for j in range(0,5):
				if(int(l[j][0])==id):
					ans=l[j][1]
					break
			if(ansc==ans):
				count=count + 1
		result=int(count)/5*100
	return render(request,'result/result_display.html',{'res':res ,'result':result})
