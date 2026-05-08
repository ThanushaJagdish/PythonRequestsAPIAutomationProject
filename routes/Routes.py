class Routes:
    BASE_URL = "https://fakestoreapi.com/"

    #products
    GET_ALL_PRODUCTS = "/products"
    GET_PRODUCT_BY_ID = "/products/{id}"
    GET_PRODUCTS_WITH_LIMIT = "/products?limit={limit}"
    GET_PRODUCTS_SORTED = "/products?sort={order}"
    GET_ALL_CATEGORIES = "/products/categories"
    GET_PRODUCTS_BY_CATEGORY = "/products/category/{category}"
    CREATE_PRODUCT = "/products"
    UPDATE_PRODUCT = "/products/{id}"
    DELETE_PRODUCT = "/products/{id}"

    #users
    GET_ALL_USERS = "/users"
    GET_USER_BY_ID = "/users/{id}"
    GET_USERS_WITH_LIMIT = "/users?limit={limit}"
    GET_USERS_SORTED = "/users?sort={order}"
    CREATE_USER = "/users"
    UPDATE_USER = "/users/{id}"
    DELETE_USER = "/users/{id}"

    #cart
    GET_ENTIRE_CART = "/carts"
    GET_CART_BY_ID = "/carts/{id}"
    GET_CART_WITH_LIMIT = "/carts?limit=x"
    GET_CART_SORTED = "/carts?sort={order}"
    GET_CART_BASED_ON_DATE = "/carts?startDate={start-date}&endDate={end-date}"
    GET_CART_BY_USERID = "/carts/user/{userId}"
    CREATE_A_CART = "/carts"
    UPDATE_A_CART = "/carts/{id}"
    PARTIAL_UPDATE_A_CART = "/carts/{id}"
    DELETE_A_CART = "/carts/{id}"
