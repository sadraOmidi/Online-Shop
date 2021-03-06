PGDMP     +                    z           Online_Shop    14.2    14.2                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16715    Online_Shop    DATABASE     q   CREATE DATABASE "Online_Shop" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
    DROP DATABASE "Online_Shop";
                postgres    false            ?            1259    16725    admin    TABLE     ?   CREATE TABLE public.admin (
    "ID" integer NOT NULL,
    email character varying(250) NOT NULL,
    password character varying(100) NOT NULL,
    city character varying(50) NOT NULL,
    province character varying(50) NOT NULL
);
    DROP TABLE public.admin;
       public         heap    postgres    false            ?            1259    16724    admin_ID_seq    SEQUENCE     ?   ALTER TABLE public.admin ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."admin_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    212            ?            1259    16733    product    TABLE     ?   CREATE TABLE public.product (
    "ID" integer NOT NULL,
    product_code integer,
    product_name character varying(100) NOT NULL,
    product_price numeric NOT NULL,
    count numeric NOT NULL,
    admin_id integer NOT NULL
);
    DROP TABLE public.product;
       public         heap    postgres    false            ?            1259    16732    product_ID_seq    SEQUENCE     ?   ALTER TABLE public.product ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."product_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    214            ?            1259    16717    user    TABLE     #  CREATE TABLE public."user" (
    "ID" integer NOT NULL,
    name character varying(50) NOT NULL,
    city character varying(50) NOT NULL,
    province character varying(50) NOT NULL,
    email character varying(250) NOT NULL,
    password character varying(250) NOT NULL,
    mobile text
);
    DROP TABLE public."user";
       public         heap    postgres    false            ?            1259    16716    user_ID_seq    SEQUENCE     ?   ALTER TABLE public."user" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."user_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    210            ?          0    16725    admin 
   TABLE DATA           F   COPY public.admin ("ID", email, password, city, province) FROM stdin;
    public          postgres    false    212   ?       ?          0    16733    product 
   TABLE DATA           c   COPY public.product ("ID", product_code, product_name, product_price, count, admin_id) FROM stdin;
    public          postgres    false    214           ?          0    16717    user 
   TABLE DATA           U   COPY public."user" ("ID", name, city, province, email, password, mobile) FROM stdin;
    public          postgres    false    210   ?                  0    0    admin_ID_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public."admin_ID_seq"', 7, true);
          public          postgres    false    211                       0    0    product_ID_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public."product_ID_seq"', 7, true);
          public          postgres    false    213                       0    0    user_ID_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public."user_ID_seq"', 12, true);
          public          postgres    false    209            i           2606    16731    admin admin_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.admin
    ADD CONSTRAINT admin_pkey PRIMARY KEY ("ID");
 :   ALTER TABLE ONLY public.admin DROP CONSTRAINT admin_pkey;
       public            postgres    false    212            m           2606    16739    product product_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pkey PRIMARY KEY ("ID");
 >   ALTER TABLE ONLY public.product DROP CONSTRAINT product_pkey;
       public            postgres    false    214            g           2606    16723    user user_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY ("ID");
 :   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_pkey;
       public            postgres    false    210            j           1259    16828    fki_admin_id    INDEX     D   CREATE INDEX fki_admin_id ON public.product USING btree (admin_id);
     DROP INDEX public.fki_admin_id;
       public            postgres    false    214            k           1259    16745    fki_s    INDEX     =   CREATE INDEX fki_s ON public.product USING btree (admin_id);
    DROP INDEX public.fki_s;
       public            postgres    false    214            n           2606    16823    product admin_id    FK CONSTRAINT     |   ALTER TABLE ONLY public.product
    ADD CONSTRAINT admin_id FOREIGN KEY (admin_id) REFERENCES public.admin("ID") NOT VALID;
 :   ALTER TABLE ONLY public.product DROP CONSTRAINT admin_id;
       public          postgres    false    3177    212    214            ?   \  x???1n1Ek?)|C?D???
??P"?Y?gǘMħ???$ud????}W?M????ؿ??Mϯ?}?BVKTW\9?Q?QS????E???ll)E'??z?????z?u???ׇC????`X???Į?o_8?^Q?-?	(Ur?Ҋ?,ں8qT? ?7Hq(feq?ί?}?%??'??S?}?-΍?D????<?Si-?V?????ђ? ??I3??Q9\?v??oCg_(躩??"??6i(???$]???)F?c?R?@o9jA??/??m2??b??%#Lu??3??4ʑhD.?㌨%??3U?4j+]2?.~l?L>?R&???o??U?+???qY?_ߵu      ?   Z   x?ʻ?0???< ;'? *?(???E??)??O??p?q?sz!?ȌDY???PJ.?`X???4z/Zm??uu[Qh????0?      ?   
  x????n?0E???"EJ?.??E7??$3?,??/ǝ???7???M??r?n}????K??uYק?^&?????0z?j	T????*?^???W?%?
C??)@J%??S?M??e????6]?C?M??ovz^?o?u};?l?K,?!??$Vr??)?Zc???)E0Uq??????????9Mz>M?r??c?????|}??1++JRGp?$A???%?)vU??F?ja?^?HJw????8äf???[?.??q???EO??	?{6?[ l%????g%pО?Q??Y'??Kb?b??#Y?(?a??+[???ۑ??/W??V?P9x3?!I#Mk?X???2r????5?74c???O??Nô???M??6?????<???z[??ܘ?֑%??dd?Q)5??k??cĨVԗ???R? KA<??	?????sǮ?׿!??!jM??j?????Վ?3I?pL^?*bD||x?-W?4??P???`???1???Ǜ????1???i??_?-?     