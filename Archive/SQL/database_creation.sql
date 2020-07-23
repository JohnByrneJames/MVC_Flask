CREATE TABLE [Users] (
	[userID] Int IDENTITY NOT NULL,
	[firstName] VarChar(200) NULL,
	[surname] VarChar(200) NULL,
	[username] VarChar(500) NOT NULL,
	[password] VarChar(500) NOT NULL,
	PRIMARY KEY ([userID])
);

CREATE TABLE [Quiz] (
	[quizID] Int IDENTITY NOT NULL,
	[timeToComplete] Time NOT NULL,
	[score] Int NULL,
	[maxScore] Int NOT NULL,
	[overviewFile] VarChar(300) NULL,
	PRIMARY KEY ([quizID])
);

CREATE TABLE [UsersQuiz] (
	[userID] Int NOT NULL,
	[quizID] Int NOT NULL,
	CONSTRAINT user_quiz_pk PRIMARY KEY (userID, quizID),
	CONSTRAINT FK_userID
		FOREIGN KEY (userID) REFERENCES Users (userID),
	CONSTRAINT FK_quizID
		FOREIGN KEY (quizID) REFERENCES Quiz (QuizID)
);