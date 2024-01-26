create table PhysicalTrainers(
    PTID int primary key ,
    Fname char,
    Lname char,
    clinicID int
    
);

create table PatientInfo(
    custID int primary key,
    Fname char,
    Lname char,
    phone double,
    insured bool,
    apptsRemaining int
);

create table Appointments(
    aptID int primary key,
    custID int key,
    PTID int key,
    aptTime time
    
);


create table Workouts(
    workoutID int primary key,
    custID int key,
    exercise char key,
    numbSets int,
    numbReps int
);

create table Exercises(
    exercise char,
    tools char
);
