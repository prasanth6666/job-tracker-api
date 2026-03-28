from sqlalchemy import Column,Integer,String,DateTime,Text
from sqlalchemy.sql import func
from database.database import Base

class Job(Base):
    
    __tablename__= "jobs"
    id = Column(
        Integer, 
        primary_key=True,
        index=True)

    company = Column(
        String(255), 
        nullable=False,
        index=True,  # Index for faster searching
        comment="Name of the company"
    )
    
    # Job position/title - required field
    position = Column(
        String(255), 
        nullable=False,
        index=True,
        comment="Job position or title"
    )
    
    # Application status - has default value
    status = Column(
        String(50), 
        nullable=False,
        default="applied",
        index=True,  # Index because we'll filter by this often
        comment="Current status: applied, interviewing, offer, rejected, accepted"
    )
    
    # Date when application was submitted
    date_applied = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),  # Auto-set to current timestamp
        comment="Date and time when application was submitted"
    )
    
    # Optional notes about the application
    notes = Column(
        Text,  # Text allows unlimited length (vs String which has limit)
        nullable=True,
        comment="Additional notes about the application"
    )
    
    # Timestamp for when record was created
    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        comment="When this record was created in database"
    )
    
    # Timestamp for when record was last updated
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),  # Auto-update when record changes
        comment="When this record was last updated"
    )
    

    
    def __repr__(self):
        """
        String representation of Job object
        Useful for debugging
        """
        return f"<Job(id={self.id}, company='{self.company}', position='{self.position}', status='{self.status}')>"
    