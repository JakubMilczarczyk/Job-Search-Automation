# Job Search Automation Project

Welcome to the Job Application Automation Project! 

This project has several objectives:
- **Automate** the search and application process for job opportunities in the IT field.
- **Gain hands-on experience** with cloud and data engineering tools.
- **Prepare for the AWS Data Analytics Certification** by building a practical pipeline that simulates real-world data tasks.

## Project Overview

The Job Application Automation Project automates web scraping for job listings, processes and stores data in AWS, and ultimately assists with data analysis and dashboarding. The project will use Python, Docker, AWS services (such as S3, Glue, and Redshift), and Airflow for orchestration, enabling a full data pipeline from data collection to visualization.

## Tech Stack

This project uses the following technologies:
- **Python**: For data collection scripts and automation.
- **AWS (Amazon Web Services)**: Including S3, IAM, Glue, Redshift, and potentially Kinesis for data management and analysis.
- **Docker**: To containerize scraping scripts for consistent, reproducible execution.
- **Apache Airflow**: For managing and automating data pipelines.
- **Git**: For version control and project management.

## Project Structure

```
job_application_automation/
├── scrapers/                 # Python scripts for scraping job postings
├── docker/                   # Docker configuration files (Dockerfile, docker-compose)
├── aws_configs/              # Configuration files for AWS (IAM roles, policies, etc.)
├── data/                     # Local storage for raw and processed data (ignored by .gitignore)
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies
```

## Getting Started

### Prerequisites

1. **AWS Account**: Ensure you have an AWS account with access to Free Tier services.
2. **Docker**: Install Docker on your local machine. Follow instructions at [Docker's official site](https://docs.docker.com/get-docker/).
3. **Python 3.8+**: Ensure you have Python installed, with `pip` for managing dependencies.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/job_application_automation.git
   cd job_application_automation
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Docker:**
   - Build the Docker image for the scraper scripts.
   ```bash
   docker build -t job-scraper .
   ```

### AWS Setup

1. **Create an S3 Bucket**:
   - In your AWS Console, create a new bucket for storing raw and processed job data.

2. **IAM Configuration**:
   - Set up an IAM user with restricted permissions to S3 and any other required AWS services.
   - Add the generated access keys to your environment variables or a configuration file (ensuring it's excluded from Git with `.gitignore`).

### Running the Project

To run the scraping scripts in Docker and upload results to AWS:

1. **Run the Docker container** for scraping:
   ```bash
   docker run --env-file ./aws_configs/.env job-scraper
   ```

2. **Monitor** the AWS S3 bucket to check that the scraped data is uploaded correctly.

## Future Plans

- **Integration with Apache Airflow**: Orchestrate scraping and ETL tasks in Airflow to schedule and automate the data pipeline.
- **Real-time Data Processing**: Add Kinesis and Glue Streaming to enable near-real-time data updates.
- **Data Analytics**: Store and analyze job data in Redshift, and visualize trends with AWS Quicksight.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

By following this README, you can set up, run, and develop the project further, enhancing your skills and progressing toward your certification and career goals. Good luck!
```

