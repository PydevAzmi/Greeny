System :
    - products
    - accounts [activation:email]
    - orders , track order 
    - coupons 
    - payments
    - dashboard
    -------------------------
    - celery , redis
    - caching 
    - optmization 
    - django command 
    - translation 
    - ajax 
    - docker 
    - deploy [heroku - aws]
    -------------------------
    - API
    - Docs
    ---------------------------------

Products : 

    - name 
    - sku 
    - brand        * [name-img]
    - images       *
    - subtitle
    - description 
    - tags         * package 
    - price
    - flag [new-sale-feature] dropdown
    - quanitity 
    - reviews      * [user_id-product_id-rate[0:5]-feedback ,datetime]     
    - category     * [name -img]


Order : 
    - status [recieved,processed,shipped,delivered]
    - user 
    - id
    - total items 
    - delivery time
    - order time 
    - total 
    - sub_total

OrderDetail : 
    - order_id
    - product_id
    - price
    - quantity 
    - total 


User : 
    - address *
    - name
    - email 
    - image 
    - phone_number *
---------------------------------------------------
    - resuable apps 
    - signle apps 
    - 3
