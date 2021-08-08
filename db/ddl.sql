drop table if exists T_MAP;
create table T_MAP (
    CX real
    , CY integer
    , VAL real
    , primary key(CX, CY)
);