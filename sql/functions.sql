CREATE OR REPLACE FUNCTION get_companies_gist(integer, integer)
RETURNS TABLE(id integer, title varchar(60), foundation_date date)
LANGUAGE SQL
AS $$ 
    SELECT company_id, name, foundation_date
    FROM companies
    LIMIT $1
    OFFSET $2;
$$;

CREATE OR REPLACE FUNCTION post_company(title varchar(60),
                                        foundation_date date,
                                        descr varchar(2000) default null,
                                        ceo varchar(60) default null)
RETURNS integer
LANGUAGE SQL
AS $$
    INSERT INTO companies (name, description, foundation_date, ceo) VALUES
        (title, descr, foundation_date, ceo)
    RETURNING company_id;
$$;

CREATE OR REPLACE FUNCTION get_company(integer)
RETURNS TABLE(id integer, title varchar(60), ceo varchar(60), foundation_date date)
LANGUAGE SQL
AS $$
    SELECT company_id, name, ceo, foundation_date
    FROM companies
    WHERE company_id=$1;
$$;

CREATE OR REPLACE FUNCTION get_games_gist(integer, integer)
RETURNS TABLE(id integer, title varchar(60), company varchar(60), release_date date)
LANGUAGE SQL
AS $$ 
    SELECT game_id, g.name, c.name, foundation_date
    FROM games as g JOIN companies as c
    ON g.game_id=c.company_id
    LIMIT $1
    OFFSET $2;
$$;