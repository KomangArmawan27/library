# Use Node.js base image
FROM node:18

# Set the working directory
WORKDIR /frontend

# Copy package.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy Vue project files
COPY . .

# Expose Vue development server port
EXPOSE 5173

# Start Vue in development mode
CMD ["npm", "run", "dev", "--", "--host"]