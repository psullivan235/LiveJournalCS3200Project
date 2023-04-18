DROP SCHEMA IF EXISTS LiveJournalDB;
CREATE SCHEMA LiveJournalDB;
USE LiveJournalDB;

CREATE TABLE UGroups
(
    GroupID     INTEGER PRIMARY KEY auto_increment,
    Description VARCHAR(500)

);

CREATE TABLE Users
(
    UserID   INTEGER PRIMARY KEY auto_increment,
    Username varchar(100)
);

CREATE TABLE Posts
(
    PostID  INTEGER PRIMARY KEY auto_increment,
    Likes   INTEGER DEFAULT 0,
    Views   INTEGER DEFAULT 0,
    Content varchar(5000),
    PostedOn DATETIME DEFAULT NOW(),
    UserID  INTEGER,
    FOREIGN KEY (UserID) REFERENCES Users (UserID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE GroupPosts
(
    GroupID INTEGER,
    PostID  INTEGER,
    PRIMARY KEY (GroupID, PostID),
    FOREIGN KEY (GroupID) REFERENCES UGroups (GroupID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (PostID) REFERENCES Posts (PostID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE GroupMemberships
(
    GroupID INTEGER,
    UserID  INTEGER,
    PRIMARY KEY (GroupID, UserID),
    FOREIGN KEY (GroupID) REFERENCES UGroups (GroupID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (UserID) REFERENCES Users (UserID) ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE PostReactions
(
    PostID   INTEGER,
    UserID   INTEGER,
    Reaction varchar(100),
    PRIMARY KEY (PostID, UserID),
    FOREIGN KEY (PostID) REFERENCES Posts (PostID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (UserID) REFERENCES Users (UserID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Follows
(
    FollowerUserID   INTEGER,
    InfluencerUserID INTEGER,
    Friend           boolean,
    PRIMARY KEY (FollowerUserID, InfluencerUserID),
    FOREIGN KEY (FollowerUserID) REFERENCES Users (UserID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (InfluencerUserID) REFERENCES Users (UserID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE PostLikes
(
    PostID INTEGER,
    UserID INTEGER,
    PRIMARY KEY (PostID, UserID),
    FOREIGN KEY (PostID) REFERENCES Posts (PostID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (UserID) REFERENCES Users (UserID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Company
(
    CompanyID          INTEGER auto_increment,
    Name               varchar(100),
    ProductDescription varchar(500),
    PRIMARY KEY (CompanyID)
);

CREATE TABLE Sponsorship
(
    CompanyID    INTEGER,
    UserID       INTEGER,
    Compensation varchar(500),
    PRIMARY KEY (CompanyID, UserID),
    FOREIGN KEY (CompanyID) REFERENCES Company (CompanyID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (UserID) REFERENCES Users (UserID) ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE Advertisements
(
    AdID        INTEGER auto_increment,
    Name        varchar(100),
    Description varchar(500),
    Content     varchar(500),
    Views       INTEGER DEFAULT 0,
    CompanyID   INTEGER,
    PRIMARY KEY (AdID),
    FOREIGN KEY (CompanyID) REFERENCES Company (CompanyID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE UserMetadata
(
    MetadataID     INTEGER auto_increment,
    TotalPostViews INTEGER,
    AvgPostViews   INTEGER,
    TimeOnSite     DATETIME,
    UserID         INTEGER,
    PRIMARY KEY (MetadataID),
    FOREIGN KEY (UserID) REFERENCES Users (UserID) ON UPDATE CASCADE ON DELETE CASCADE
);


