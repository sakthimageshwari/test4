create database testportal;
use testportal;

CREATE TABLE members_regform (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fname VARCHAR(255) NOT NULL,
    lname VARCHAR(255) NOT NULL,
    gender VARCHAR(255) NOT NULL,
    dob DATE NOT NULL,
    phone INT NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    uname VARCHAR(255) NOT NULL UNIQUE,
    passcode VARCHAR(255) NOT NULL
);

CREATE TABLE members_q_a (
    id INT AUTO_INCREMENT PRIMARY KEY,
    subject VARCHAR(255) NOT NULL,
    question VARCHAR(255) NOT NULL,
    option_1 VARCHAR(255) NOT NULL,
    option_2 VARCHAR(255) NOT NULL,
    option_3 VARCHAR(255) NOT NULL,
    option_4 VARCHAR(255) NOT NULL,
    answer VARCHAR(255) NOT NULL
);

select * from members_regform;
drop table members_q_s;
alter table members_q_a add subject varchar(20);
insert into members_q_a values(1,"what is the value of 2+2","2","4","6","2","option b","aptitude");
INSERT INTO members_q_a VALUES
(2, "What is the next number in the series: 2, 4, 8, 16, ?", "18", "20", "32", "24", "option c", "aptitude"),
(3, "If a train travels 60 km in 1.5 hours, what is its speed?", "30 km/h", "40 km/h", "45 km/h", "50 km/h", "option c", "aptitude"),
(4, "A man buys an item for ₹500 and sells it for ₹600. What is the profit percentage?", "10%", "15%", "20%", "25%", "option d", "aptitude"),
(5, "What is the average of 10, 20, 30, 40, and 50?", "25", "30", "35", "40", "option b", "aptitude"),
(6, "If 5x = 20, what is the value of x?", "2", "3", "4", "5", "option c", "aptitude"),
(7, "A shopkeeper gives 10% discount on ₹200. What is the selling price?", "₹180", "₹190", "₹185", "₹175", "option a", "aptitude"),
(8, "What is the simple interest on ₹1000 at 5% per annum for 2 years?", "₹50", "₹100", "₹150", "₹200", "option b", "aptitude"),
(9, "If the perimeter of a square is 40 cm, what is the length of one side?", "8 cm", "10 cm", "12 cm", "14 cm", "option b", "aptitude"),
(10, "A car covers 150 km in 3 hours. What is its average speed?", "40 km/h", "45 km/h", "50 km/h", "55 km/h", "option c", "aptitude");
select * from members_q_a;
INSERT INTO members_q_a VALUES
(11, "What is the chemical symbol for water?", "H2", "H2O", "HO2", "OH", "option b", "science"),
(12, "Which part of the plant conducts photosynthesis?", "Root", "Stem", "Leaf", "Flower", "option c", "science"),
(13, "What gas do humans exhale?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen", "option b", "science"),
(14, "Which planet is known for its rings?", "Mars", "Jupiter", "Saturn", "Venus", "option c", "science"),
(15, "What is the boiling point of water at sea level?", "90°C", "95°C", "100°C", "110°C", "option c", "science"),
(16, "Which organ pumps blood throughout the body?", "Lungs", "Liver", "Heart", "Kidney", "option c", "science"),
(17, "What is the main gas in Earth's atmosphere?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen", "option c", "science"),
(18, "Which vitamin is produced when skin is exposed to sunlight?", "Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D", "option d", "science"),
(19, "What is the center of an atom called?", "Electron", "Proton", "Nucleus", "Neutron", "option c", "science"),
(20, "Which force keeps us on the ground?", "Magnetism", "Friction", "Gravity", "Electricity", "option c", "science");

select min(id) from members_q_a where subject="aptitude";
select min(id) from members_q_a where subject="science";

