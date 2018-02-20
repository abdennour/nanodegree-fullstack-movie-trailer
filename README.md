# Movie Trailer

Source code for a Movie Trailer website.


## Getting Started

### Prerequisites

- Python 2.7

### Installing

To get a development environment running, execute the following command line :

```sh
python src/entertainment_center.py

```

The command above generates HTML page of movies list and open this page in your default browser.


## Running the tests

We are working on introducing unit-tests for the next period.


## Deployment

It is a single page static website deployment.
This page is `fresh_tomatoes.html` under the project root folder.
Before deployment, make sure this page/file is generated and up-to-date.

```sh
# Make "fresh_tomatoes.html" up-to-date
python src/entertainment_center.py

# e.g: Deploy to S3
aws s3 cp fresh_tomatoes.html s3://$YOUR_BUCKET/index.html

# e.g: Deploy to your Server
scp -i $YOUR_SSH_PRIVATE_KEY fresh_tomatoes.html ubuntu@your-server-ip:/var/www/html/index.html

```


## Contributing

Please read [CONTRIBUTING.md](#CONTRIBUTING.md) for details on our code and the process of handling pull requests.

## Authors

* **Abdennour TOUMI** - *Orginal Author* - [in.abdennoor.com](http://in.abdennoor.com)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
