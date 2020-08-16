/* Inserting Films */

INSERT INTO Films (name, description, release_date, stars, genres, director, imdb_rating, metascore, country)
VALUES('Inception',
        'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of
         planting an idea into the mind of a C.E.O.',
         '7/29/2010',
         'Leonardo Di Caprio, Tom Hardy',
         'Action, Sci-Fi',
         'Christopher Nolan',
         8.8,
         74,
         'USA'),
	('The Dark Knight',
        'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one
        of the greatest psychological and physical tests of his ability to fight injustice.',
         '7/29/2008',
         'Christian Bale, Heath Ledger',
         'Action, Crime',
         'Christopher Nolan',
         9,
         84,
         'USA'),
	('Memento',
        'A man with short-term memory loss attempts to track down his wifes murderer.',
         '2/7/2002',
         'Guy Pearce', 'Joe Pantoliano',
         'Mystery, Crime',
         'Christopher Nolan',
         8.4,
         80,
         'USA');

/* Inserting Shows */

INSERT INTO Shows (name, description, release_year, end_year, stars, genres, creator, imdb_rating, country)
VALUES('Game of Thrones',
        'Nine noble families fight for control over the lands of Westeros, while an ancient enemy returns
         after being dormant for millennia.',
         2011,
         2019,
         'Emilia Clarke', 'Kit Harington',
         'Action, Adventure',
         'David Benioff',
         8.4,
         'USA'),
		 ('Breaking Bad',
         'A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling
         methamphetamine in order to secure his familys future.',
         2008,
         2013,
         'Bryan Cranston', 'Aaron Paul',
         'Crime, Drama',
         'Vince Gilligan',
         9.5,
         'USA')