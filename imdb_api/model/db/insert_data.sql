/* Inserting Film Titles */

INSERT INTO public."Titles"(type, name, description, release_year, stars, genres, rating, country, price)
VALUES('Film',
	   'Inception',
        'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of
         planting an idea into the mind of a C.E.O.',
         2010,
         'Leonardo Di Caprio, Tom Hardy',
         'Action, Sci-Fi',
         8.8,
         'USA',
         100),
	('Film',
	 'The Dark Knight',
        'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one
        of the greatest psychological and physical tests of his ability to fight injustice.',
         2008,
         'Christian Bale, Heath Ledger',
         'Action, Crime',
         9,
         'USA',
         75);

INSERT INTO public."Films"(
	title_id, director, metascore, duration)
	VALUES (1, 'Cristopher Nolan', 80, 135);

INSERT INTO public."Films"(
	title_id, director, metascore, duration)
	VALUES (2, 'Cristopher Nolan', 90, 145);


/* Inserting Shows Titles*/

INSERT INTO public."Titles" (type, name, description, release_year, stars, genres, rating, country, price)
VALUES('Show',
        'Game of Thrones',
        'Nine noble families fight for control over the lands of Westeros, while an ancient enemy returns
         after being dormant for millennia.',
         2011,
         'Emilia Clarke, Kit Harington',
         'Action, Adventure',
         8.4,
         'USA',
         100),
		 ('Show',
		 'Breaking Bad',
         'A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling
         methamphetamine in order to secure his familys future.',
         2008,
         'Bryan Cranston, Aaron Paul',
         'Crime, Drama',
         9.5,
         'USA',
         120);

INSERT INTO public."Shows"(
	title_id, creator, end_year)
	VALUES (3, 'David Benioff', 2019);

INSERT INTO public."Shows"(
	title_id, creator, end_year)
	VALUES (4, 'Vince Gilligan', 2013);


/* Inserting Episodes Titles*/

INSERT INTO public."Titles" (type, name, description, release_year, stars, genres, rating, country, price)
VALUES('Episode',
        'Winterfell',
        'Jon and Daenerys arrive in Winterfell and are met with skepticism. Sam learns about the fate of his family.
         Cersei gives Euron the reward he aims for. Theon follows his heart.',
         2011,
         'Emilia Clarke, Kit Harington',
         'Action, Adventure',
         7.5,
         'USA',
         30),
         ('Episode',
        'The Kingsroad',
        'While Bran recovers from his fall, Ned takes only his daughters to Kings Landing.
         Jon Snow goes with his uncle Benjen to the Wall. Tyrion joins them.',
         2011,
         'Emilia Clarke, Kit Harington',
         'Action, Adventure',
         8.8,
         'USA',
          25),
		 ('Episode',
		 'Pilot',
         'Diagnosed with terminal lung cancer, chemistry teacher Walter White teams up with
         former student Jesse Pinkman to cook and sell crystal meth.',
         2008,
         'Bryan Cranston, Aaron Paul',
         'Crime, Drama',
         9.0,
         'USA',
         30);


INSERT INTO public."Episodes"(
	title_id, show_id, season, duration, number)
	VALUES (5, 3, 1, 62, 1);

INSERT INTO public."Episodes"(
	title_id, show_id, season, duration, number)
	VALUES (7, 3, 1, 61, 1);

INSERT INTO public."Episodes"(
	title_id, show_id, season, duration, number)
	VALUES (6, 4, 2, 60, 1);