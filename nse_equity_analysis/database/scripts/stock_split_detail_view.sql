-- View: public.stock_split_detail

-- DROP VIEW public.stock_split_detail;

CREATE OR REPLACE VIEW public.stock_split_detail AS
 SELECT ec.id AS equity_id,
    es.company_name,
    es.record_date,
    es.split_date,
    es.face_value_before,
    es.face_value_after
   FROM equity_split es,
    equity_code ec
  WHERE btrim(upper("substring"(es.company_name::text, 0, "position"(es.company_name::text, ' Ltd'::text)))) = btrim(upper("substring"(ec.name::text, 0, "position"(ec.name::text, ' Lim'::text)))) AND btrim(upper("substring"(es.company_name::text, 0, "position"(es.company_name::text, ' Ltd'::text)))) IS NOT NULL AND btrim(upper("substring"(es.company_name::text, 0, "position"(es.company_name::text, ' Ltd'::text)))) <> ''::text;

ALTER TABLE public.stock_split_detail
    OWNER TO postgres;


