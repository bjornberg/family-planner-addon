ARG BUILD_FROM
FROM $BUILD_FROM

# Install Python and Flask
RUN apk add --no-cache \
    python3 \
    py3-pip \
    && pip3 install --no-cache-dir \
        flask==3.0.0 \
        flask-cors==4.0.0

# Set working directory
WORKDIR /app

# Copy files
COPY server.py /app/
COPY family-planner.html /app/
COPY run.sh /app/

# Make run script executable
RUN chmod a+x /app/run.sh

# Expose port
EXPOSE 5000

# Run
CMD [ "/app/run.sh" ]
