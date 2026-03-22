from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate


class ProjectCRUD:
    async def create(
        self,
        session: AsyncSession,
        data: ProjectCreate,
        owner_id: int,
    ) -> Project:
        project = Project(
            name=data.name,
            description=data.description,
            owner_id=owner_id,
        )
        session.add(project)
        await session.commit()
        await session.refresh(project)
        return project

    async def get_by_id(
        self,
        session: AsyncSession,
        project_id: int,
    ) -> Project | None:
        result = await session.execute(
            select(Project).where(Project.id == project_id)
        )
        return result.scalar_one_or_none()

    async def get_all_by_owner(
        self,
        session: AsyncSession,
        owner_id: int,
    ) -> list[Project]:
        result = await session.execute(
            select(Project).where(Project.owner_id == owner_id)
        )
        return list(result.scalars().all())

    async def update(
        self,
        session: AsyncSession,
        project: Project,
        data: ProjectUpdate,
    ) -> Project:
        update_data = data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(project, field, value)

        await session.commit()
        await session.refresh(project)
        return project

    async def delete(
        self,
        session: AsyncSession,
        project: Project,
    ) -> None:
        await session.delete(project)
        await session.commit()


crud_project = ProjectCRUD()