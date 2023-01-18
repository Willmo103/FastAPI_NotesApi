from sqlalchemy import Column, String, Integer, TIMESTAMP, text, ForeignKey
from app.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False
    )

    password = Column(
        String,
        nullable=False
    )

    name = Column(
        String,
        nullable=False
    )

    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("now()")
    )



class Note(Base):
    __tablename__ = "note"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False
    )

    owner_id = Column(
        Integer,
        ForeignKey(
            "user.id",
            ondelete="CASCADE"
        ),
        nullable=True,
    )

    content = Column(
        String,
        nullable=True
    )

    title = Column(
        String,
        nullable=False
    )

    created_at = Column(
        TIMESTAMP(
            timezone=True
        ),
        nullable=False,
        server_default=text("now()")
    )

