from idlelib import query
from unittest.mock import patch

from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

from clients.exercises.exercises_schema import CreateExerciseSchema, UpdateExerciseSchema, CreateExerciseResponseSchema, \
    GetExercisesResponseSchema
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class  Exercise(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExercisesResponseDict(TypedDict):
    exercises : list[Exercise]

class GetExerciseResponseDict(TypedDict):
    exercise:Exercise

class GetExercisesQueryDict(TypedDict):
    courseId:str

class CreateExerciseDict(TypedDict):
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str | None

class CreateExerciseResponseDict(TypedDict):
    exercise : Exercise

class UpdateExerciseDict(TypedDict):
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):
    def get_exercises_api(self,query) ->Response:
        return self.get('/api/v1/exercises',params=query)

    def get_exercise_api(self,exercise_id:str) -> Response:
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def create_exercise_api(self,request:CreateExerciseSchema)->Response:
        return self.post(f'/api/v1/exercises',json=request.model_dump(by_alias=True))

    def update_exercise_api(self,request:UpdateExerciseSchema, exercise_id:str) -> Response:
        return self.patch(f"/api/v1/exercise/{exercise_id}",json=request.model_dump(by_alias=True))

    def delete_exercise_api(self,exercise_id:str) -> Response:
        return self.delete(f"/api/v1/exercise/{exercise_id}")

    def create_exercise(self,request:CreateExerciseSchema) ->CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(self,query) ->GetExercisesResponseSchema:
        response = self.get_exercise_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise(self,exercise_id:str) -> GetExercisesResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExercisesResponseSchema.model_validate_json(response.text)



def get_exercises_client(user:AuthenticationUserSchema) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))