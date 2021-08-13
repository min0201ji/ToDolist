from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect # 특정 url을 재 요청해주는 함수
from django.urls import reverse # 기존 요청임을 의미하는 함수
from .models import *
# Create your views here.

def index(request) :
    # DB의 m̆̈y_to_do_app_todo 테이블에서 모든 row를 select
    todos = Todo.objects.all() # = select * from my_to_do_app_todo;

    # template 으로 전달할 dict 구성
    content = {'todos':todos} # index.html에서 동적으로 코드를 생성할때 dict를 사용

    return render(request,'my_to_do_app/index.html',content) # Templates/my_to_do_app/index.html
    # return HttpResponse('my_to_do_app first page') # 응답하는지 확인할 수 있는 코드
    # 요청에 대한 응답객체를 생성해서 바로 클라이언트로 반환

def createTodo(request) :
    # 사용자가 메모에 입력해서 넘긴 값을 반환하는 코드
    user_input_str = request.POST['todoContent']
    # 사용자가 전달해 준 값을 contect 파라미터의 연수로 넘겨주고 객체 인스턴스를 생성
    new_todo = Todo(content=user_input_str) # modela에 대입: insert into _todo (content) values (input_str)
    new_todo.save() # DB에 반영

    return HttpResponseRedirect(reverse('index')) # 127.0.0.1:8000 요청해야 함
    # return HttpResponse('입력한 메모 data는: '+ user_input_str + "는 DB에 저장되었습니다.")
    # return HttpResponse('createTodo 메모 작성 합니다~') # 요청에 응답하는지만 확인

def doneTodo(request) :
    # 삭제할 메모의 id 저장
    done_todo_id = request.GET['todoNum']
    print('완료한 메모의 id', done_todo_id)
    todo = Todo.objects.get(id=done_todo_id) # 넘어온 done_todo_id 의 동일한 기본키를 찾아 해당 레코드를 반환
    todo.delete() # 반환된 객체에 대해 delete 진행
    return HttpResponseRedirect(reverse('index'))


