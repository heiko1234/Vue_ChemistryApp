
# postgres_ideefix.py



from fastapi import APIRouter, Depends, HTTPException, status

from pydantic import BaseModel
from typing import Optional

from utilities.postgres_connection import execute_sql

router = APIRouter()


class Idea(BaseModel):
    name: str
    email: str
    short_title: str
    idea_description: str


class IdeaFilter(BaseModel):
    name: Optional[str] = None
    short_title: Optional[str] = None
    idea_description: Optional[str] = None

class IdeaVote(BaseModel):
    idea_id: int




@router.post("/submit_idea")
async def submit_idea(idea: Idea):

    # query = f"""
    # INSERT INTO ideefix_ideas (name, email, short_title, idea_description)
    # VALUES ('{idea.name}', '{idea.email}', '{idea.short_title}', '{idea.idea_description}')
    # """
    # execute_sql(query)

    try:
        sql = f"""
            INSERT INTO ideefix_ideas(name, email, short_title, idea_description)
            VALUES ('{idea.name}', '{idea.email}', '{idea.short_title}', '{idea.idea_description}')
            RETURNING idea_id;
        """

        print("isert a new idea, new idea_id")

        new_idea_id = execute_sql(sql)[0][0]
        new_idea_id

        print(f"isert a new idea, new idea_id: {new_idea_id}")

        # Insert into ideefix_idea_status with the new idea_id
        sql = f"""
            INSERT INTO ideefix_idea_status(idea_id, is_active)
            VALUES({new_idea_id}, TRUE);
        """
        execute_sql(sql)

        sql = f"""
            INSERT INTO ideefix_idea_votes(idea_id, vote_count_good, vote_count_bad)
            VALUES({new_idea_id}, 0, 0);
        """
        execute_sql(sql)


        return {"message": "Idea submitted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))



@router.get("/get_ideas")
async def get_ideas():
    query = "SELECT * FROM ideefix_ideas"
    return execute_sql(query)



@router.get("/get_idea_on_status")
async def get_idea_on_status():

    query = """
            SELECT *
            FROM ideefix_ideas
            JOIN ideefix_idea_status ON ideefix_ideas.idea_id = ideefix_idea_status.idea_id
            WHERE ideefix_idea_status.is_active = TRUE
        """

    return execute_sql(query)


@router.post("/get_active_ideas_filtered")
async def get_active_ideas_filtered(idea_filter: IdeaFilter):

    print("get_active_ideas_filtered")

    filters = []
    if idea_filter.name:
        filters.append(f"name ILIKE '%{idea_filter.name}%'")
    if idea_filter.short_title:
        filters.append(f"short_title ILIKE '%{idea_filter.short_title}%'")
    if idea_filter.idea_description:
        filters.append(f"idea_description ILIKE '%{idea_filter.idea_description}%'")

    filter_query = " AND ".join(filters) if filters else "1=1"

    # print(f"get_active_ideas_filtered: {idea_filter}")
    # print(f"get_active_ideas_filtered: {filter_query}")


    # query = f"""
    #         SELECT *
    #         FROM ideefix_ideas
    #         JOIN ideefix_idea_status ON ideefix_ideas.idea_id = ideefix_idea_status.idea_id
    #         WHERE ideefix_idea_status.is_active = TRUE
    #         AND {filter_query}
    #     """
    # query = f"""
    #         SELECT ideefix_ideas.idea_id, ideefix_ideas.name, ideefix_ideas.short_title, ideefix_ideas.idea_description
    #         FROM ideefix_ideas
    #         JOIN ideefix_idea_status ON ideefix_ideas.idea_id = ideefix_idea_status.idea_id
    #         WHERE ideefix_idea_status.is_active = TRUE
    #         AND {filter_query}
    #     """

    query = f"""
            SELECT ideefix_ideas.idea_id, ideefix_ideas.name, ideefix_ideas.short_title, ideefix_ideas.idea_description, ideefix_idea_votes.vote_count_bad, ideefix_idea_votes.vote_count_good
            FROM ideefix_ideas
            JOIN ideefix_idea_status ON ideefix_ideas.idea_id = ideefix_idea_status.idea_id
            LEFT JOIN ideefix_idea_votes ON ideefix_ideas.idea_id = ideefix_idea_votes.idea_id
            WHERE ideefix_idea_status.is_active = TRUE
            AND {filter_query}
            ORDER BY ideefix_ideas.idea_id DESC
        """


    data= execute_sql(query)


    # print(f"get_active_ideas_filtered: {query}")
    # print("get_active_ideas_filtered")
    # print(data)

    return data




@router.post("/vote_idea_good")
async def vote_idea(vote: IdeaVote):

    print("vote_idea")
    print(f"vote_idea: {vote}")

    # idea_id: int

    try:
        query = f"""
            UPDATE ideefix_idea_votes
            SET vote_count_good = vote_count_good + 1
            WHERE idea_id = {vote.idea_id}
        """
        execute_sql(query)
        return {"message": "Vote submitted successfully"}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid vote type")



@router.post("/vote_idea_bad")
async def vote_idea(vote: IdeaVote):

    print("vote_idea")
    print(f"vote_idea: {vote}")

    # idea_id: int

    try:
        query = f"""
            UPDATE ideefix_idea_votes
            SET vote_count_bad = vote_count_bad + 1
            WHERE idea_id = {vote.idea_id}
        """
        execute_sql(query)
        return {"message": "Vote submitted successfully"}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid vote type")




@router.post("/get_votes")
async def get_votes(vote: IdeaVote):

    print("get_votes")
    print(f"get_votes: {vote}")

    query = f"""
        SELECT vote_count_good, vote_count_bad
        FROM ideefix_idea_votes
        WHERE idea_id = {vote.idea_id}
    """

    return execute_sql(query)






