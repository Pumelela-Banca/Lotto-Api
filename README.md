### Lottery API (Real-Time Lottery Numbers in Django and FastAPI)

Real-time Lottery API that delivers up-to-date lottery numbers. The service is implemented using Django and FastAPI to ensure robust backend functionality. Additionally, Selenium is leveraged for automated data collection from various lottery sources.

---

#### Overview

The Lottery API provides real-time access to the latest lottery numbers from various sources. This API is designed to be fast, reliable, and easy to integrate into your applications.

#### Features

- **Real-Time Data**: Access the latest lottery numbers as soon as they are available.
- **Robust Backend**: Built with Django and FastAPI for high performance and scalability.
- **Automated Data Collection**: Utilizes Selenium to scrape and collect data from multiple lottery sources.

#### Getting Started

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Pumelela-Banca/Lotto-Api.git
    ```

#### API Endpoints

- **GET /lottery/latest**: Retrieve the latest lottery numbers.
    - **Response**:
        ```json
        {
            "lottery_name": "Powerball",
            "numbers": [5, 12, 23, 32, 45, 16],
            "date": "2024-08-17"
        }
        ```

- **GET /lottery/{lottery_name}**: Retrieve the latest numbers for a specific lottery.
    - **Parameters**:
        - `lottery_name` (string): The name of the lottery.
    - **Response**:
        ```json
        {
            "lottery_name": "Mega Millions",
            "numbers": [3, 15, 27, 42, 58, 22],
            "date": "2024-08-17"
        }
        ```


#### License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details.
