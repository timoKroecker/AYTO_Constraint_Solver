%--------------------------------------------------------------------------------
%-------------------------------------input--------------------------------------
%--------------------------------------------------------------------------------

int: num_girls;
int: num_boys;
int: num_matching_nights;
int: num_couples;

set of int: GIRLS = 1..num_girls;
set of int: BOYS = 1..num_boys;
set of int: NIGHTS = 1..num_matching_nights;
set of int: COUPLES = 1..num_couples;

array[GIRLS, BOYS] of int: input;
array[NIGHTS, COUPLES, 1..2] of int: nights_and_couples;
array[NIGHTS] of int: lights;
int: third_wheel;

%--------------------------------------------------------------------------------
%-----------------------------------variables------------------------------------
%--------------------------------------------------------------------------------

array[GIRLS, BOYS] of var 0..1: matches;

%--------------------------------------------------------------------------------
%-------------------------------basic constraints--------------------------------
%--------------------------------------------------------------------------------

%map input to matches
constraint
    forall(girl in GIRLS)(
        forall(boy in BOYS)(
            if(input[girl, boy] == 1) then matches[girl, boy] = 1 endif /\
            if(input[girl, boy] == -1) then matches[girl, boy] = 0 endif
        )
    );

%exactly one match per girl
constraint
    forall(girl in GIRLS)(
        sum(row(matches, girl)) = 1
    );

%either one match or two matches per boy
constraint
    forall(boy in BOYS)(
        sum(col(matches, boy)) = 1 \/
        sum(col(matches, boy)) = 2
    );

%--------------------------------------------------------------------------------
%--------------------------------matching nights---------------------------------
%--------------------------------------------------------------------------------

constraint
    forall(n in NIGHTS)(
        sum(c in COUPLES)(matches[nights_and_couples[n, c, 1], nights_and_couples[n, c, 2]]) = lights[n]
    );

%--------------------------------------------------------------------------------
%--------------------------------threeway couple---------------------------------
%--------------------------------------------------------------------------------

constraint
    exists(boy in BOYS)(
        third_wheel = -1 \/
        (matches[third_wheel, boy] = 1 /\
        sum(girl in GIRLS)(matches[girl, boy]) = 2)
    );