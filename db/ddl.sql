drop table if exists T_MAP;
create table T_MAP (
    CX real
    , CY integer
    , VAL real
    , primary key(CX, CY)
);

drop table if exists T_MAP2;
create table T_MAP2 (
    DT text
    , Y integer
    , VAL real
    , primary key(DT, Y)
);

