# IAM Service

A secure backend service for user registration, login, and role-based access control using FastAPI and JWT.

## Tech Stack

- Python 3.11
- FastAPI
- SQLite (Development) / PostgreSQL (Production)
- JWT for authentication
- Docker & Docker Compose
- SQLAlchemy (ORM)
- Pydantic (Data validation)
- Passlib (Password hashing)

## Setup Instructions

### Prerequisites

- Docker
- Docker Compose

### Running the Service

1. Clone the repository:
```bash
git clone <repository-url>
cd IAM-Service
```

2. Build and start the service:
```bash
docker-compose up --build
```

The service will be available at `http://localhost:8000`

### API Documentation

Once the service is running, you can access:
- Swagger UI documentation: `http://localhost:8000/docs`
- ReDoc documentation: `http://localhost:8000/redoc`

## Design Decisions

1. **Database**: SQLite is used for simplicity and development purposes. For production, consider using PostgreSQL.
2. **Authentication**: JWT tokens are used for stateless authentication.
3. **Password Security**: Passwords are hashed using bcrypt.
4. **API Structure**: RESTful API design with clear endpoint naming conventions.
5. **Environment Variables**: Configuration is managed through environment variables for flexibility.

## Development

The service is configured with hot-reload enabled, so any changes to the code will automatically restart the server.

## Security Considerations

- Change the `SECRET_KEY` in production
- Configure proper CORS settings for production
- Use HTTPS in production
- Implement rate limiting
- Add proper logging and monitoring

## Scaling Considerations

### Current Architecture
- FastAPI application with SQLite database
- Single container deployment
- In-memory JWT token validation

### Potential Bottlenecks

1. **Database**
   - SQLite is not suitable for concurrent access
   - No database replication or sharding
   - Limited connection pooling

2. **Authentication**
   - JWT token validation is CPU-intensive
   - No token blacklisting mechanism
   - No distributed session management

3. **Application**
   - Single instance deployment
   - No load balancing
   - No caching layer

### Scaling Solutions

1. **Database Scaling**
   - Migrate to PostgreSQL for production
   - Implement connection pooling
   - Set up database replication
   - Consider read replicas for heavy read operations
   - Implement database sharding for large user bases

2. **Application Scaling**
   - Deploy multiple application instances
   - Implement load balancing (e.g., Nginx, HAProxy)
   - Add Redis for caching and session management
   - Use message queues for async operations
   - Implement circuit breakers for external services

3. **Authentication Scaling**
   - Implement Redis for token blacklisting
   - Use distributed session management
   - Consider OAuth2.0 for third-party authentication
   - Implement rate limiting per user/IP

4. **Infrastructure Scaling**
   - Use Kubernetes for container orchestration
   - Implement auto-scaling based on load
   - Use CDN for static content
   - Implement proper monitoring and logging
   - Use service mesh for microservices communication

### Production Deployment Example

```yaml
# Example Kubernetes deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: iam-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: iam-service
  template:
    metadata:
      labels:
        app: iam-service
    spec:
      containers:
      - name: iam-service
        image: iam-service:latest
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: db-secrets
              key: url
        - name: REDIS_URL
          valueFrom:
            secretKeyRef:
              name: redis-secrets
              key: url
```

### Monitoring and Maintenance

1. **Metrics to Monitor**
   - Request latency
   - Error rates
   - Database connection pool usage
   - Memory usage
   - CPU utilization
   - Token validation times

2. **Maintenance Tasks**
   - Regular security updates
   - Database backups
   - Log rotation
   - Certificate renewal
   - Performance optimization

## Sample Users

The service comes pre-seeded with the following test users:

1. Admin: admin@example.com / Admin@123
2. Legal: legal@example.com / Legal@123
3. PM: pm@example.com / PM@123
4. Sales: sales@example.com / Sales@123
5. Regular User: user@example.com / User@123