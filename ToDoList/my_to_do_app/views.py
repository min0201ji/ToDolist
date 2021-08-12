from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request) :
    return render(request,'my_to_do_app/index.html') # Templates/my_to_do_app/index.html
    # return HttpResponse('my_to_do_app first page') # 응답하는지 확인할 수 있는 코드
    # 요청에 대한 응답객체를 생성해서 바로 클라이언트로 반환

def createTodo(request) :
    # 사용자가 메모에 입력해서 넘긴 값을 반환하는 코드
    user_input_str = request.POST['todoContent']
    # 사용자가 전달해 준 값을 contect 파라미터의 연수로 넘겨주고 객체 인스턴스를 생성
    new_todo = Todo(content=user_input_str) # modela에 대입: insert into _todo (content) values (input_str)
    new_todo.save() # DB에 반영

    return HttpResponse('입력한 메모 data는: '+ user_input_str)
    # return HttpResponse('createTodo 메모 작성 합니다~') # 요청에 응답하는지만 확인

