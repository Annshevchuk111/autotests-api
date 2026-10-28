from idlelib import query
from unittest.mock import patch

from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

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

class UpdateExerciseDict(TypedDict):
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):
    def get_exercises_api(self,query:GetExercisesQueryDict) ->Response:
        return self.get('/api/v1/exercises',params=query)

    def get_exercise_api(self,exercise_id:str) -> Response:
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def create_exercise_api(self,request:CreateExerciseDict)->Response:
        return self.post(f'/api/v1/exercise',json=request)

    def update_exercise_api(self,request:UpdateExerciseDict, exercise_id:str) -> Response:
        return self.patch(f"/api/v1/exercise/{exercise_id}",json=request)

    def delete_exercise_api(self,exercise_id:str) -> Response:
        return self.delete(f"/api/v1/exercise/{exercise_id}")