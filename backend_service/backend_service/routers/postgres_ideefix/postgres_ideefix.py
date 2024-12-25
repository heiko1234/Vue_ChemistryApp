
# postgres_ideefix.py



from fastapi import APIRouter, Depends, HTTPException, status

from pydantic import BaseModel

from utilities.postgres_connection import execute_sql

router = APIRouter()


class Idea(BaseModel):
    name: str
    email: str
    short_title: str
    idea_description: str


@router.post("/submit_idea")
async def submit_idea(idea: Idea):

    query = f"""
    INSERT INTO ideefix_ideas (name, email, short_title, idea_description)
    VALUES ('{idea.name}', '{idea.email}', '{idea.short_title}', '{idea.idea_description}')
    """

    try:
        execute_sql(query)
        return {"message": "Idea submitted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get("/get_ideas")
async def get_ideas():
    query = "SELECT * FROM ideefix_ideas"
    return execute_sql(query)


