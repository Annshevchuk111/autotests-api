from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import CreateExerciseDict, GetExercisesQueryDict, get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client, CreateUserRequestSchema
from tools.faker  import fake
from clients.courses.courses_client import get_courses_client
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileResponseSchema, CreateFileRequestSchema

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email= fake.email(),
    password="string",
    last_name="string",
    first_name= "string",
    middle_name="string"
)
create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthenticationUserSchema(
    email= create_user_request.email,
    password= create_user_request.password,
)

files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client =get_exercises_client(authentication_user)

create_file_request = CreateFileRequestSchema(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image.png"
)
create_file_response = files_client.create_file(create_file_request)

create_course_request = CreateCourseRequestSchema(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id
)
create_course_response = courses_client.crete_course(create_course_request)
print(create_course_response)

create_exercise_request =CreateExerciseSchema(
    courseId=create_course_response.course.id
)
print(create_exercise_request)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print(create_exercise_response)
print(create_exercise_response.exercise.course_id)

# get_exercises_response = exercises_client.get_exercises(create_exercise_response.exercise.course_id)
# print(get_exercises_response)