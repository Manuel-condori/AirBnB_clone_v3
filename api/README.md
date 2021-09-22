# API
This project consists on creating a API to manage Object resources related to AirBnB

**Useful links**
- [Learn REST: A RESTful Tutorial](https://www.restapitutorial.com/)
- [Designing a RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
- [HTTP access control (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
- [Flask cheatsheet](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/301/flask_cheatsheet.pdf)
- [What are Flask Blueprints, exactly?](https://stackoverflow.com/questions/24420857/what-are-flask-blueprints-exactly)
- [Flask](https://palletsprojects.com/p/flask/)
- [Modular Applications with Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/)
- [Flask tests](https://flask.palletsprojects.com/en/1.1.x/testing/)
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/)
- [AirBnB clone - RESTful API](https://www.youtube.com/watch?v=LrQhULlFJdU&feature=youtu.be)

**Github and review related**
- [Why code reviews matter (and actually save time!)](https://www.atlassian.com/agile/software-development/code-reviews)
- [Code Review Best Practices](https://www.kevinlondon.com/2015/05/05/code-review-best-practices.html)
- [GitHub - code review tool](https://github.com/features#code-review)
- [Code Review on GitHub](https://www.youtube.com/watch?v=HW0RPaJqm4g)
- [Effective pull requests and other good practices for teams using GitHub](https://codeinthehole.com/tips/pull-requests-and-other-good-practices-for-teams-using-github/)
- [Merging vs. Rebasing](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)

**Run the tests for FileStorage**
```bash
$ python3 -m unittest discover tests
```

**Run the tests for DBStorage**
```bash
$ HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests
```

### Start the service
- Goto the root folder of the repo and run
```bash
$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 python3 -m api.v1.app
```

### Check if the service is runnig OK
```bash
$ curl -X GET http://0.0.0.0:5000/api/v1/status
{
  "status": "OK"
}
$
$ curl -X GET -s http://0.0.0.0:5000/api/v1/status -vvv 2>&1 | grep Content-Type
< Content-Type: application/json
$
```

### Get some stats of the resources
```bash
$ curl -X GET http://0.0.0.0:5000/api/v1/stats
```

### See the documentation
After start the service go to `http://0.0.0.0:5000/apidocs` in your browser and you'll see a
