USE deep_hard;
CREATE TABLE Events(
    EventId int NOT NULL AUTO_INCREMENT,
    PageId varchar(255) NOT NULL,
    Label varchar(255),
    PRIMARY KEY (EventId)
)