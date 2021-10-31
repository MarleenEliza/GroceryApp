# Build Backend

## 1. activate virtual environment

```
$ cd server
$ source env/bin/activate
```

OUTPUT:

```
# command line will have (env) in front of it
```

<br/>

## 2. activate app

```
$ python3 app.py
```

OUTPUT:

```
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 224-389-813
```

<br/>

# Build Front-End

## 1. install setup

```
$ cd client
$ npm install
```

<br/>

## 2a Compile and hot-reload for development

```
npm run serve
```

<br/>

## 2b Compiles and minifies for production

```
npm run build
```
