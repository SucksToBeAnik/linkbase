# Base build stage
FROM node:latest AS build

WORKDIR /app

COPY package*.json ./

# Install dependencies
RUN npm install

COPY . .

FROM node:bullseye-slim AS dev

WORKDIR /app

COPY --from=build /app /app

# Expose development server port
EXPOSE 3000

# Run the development server
CMD ["npm", "run", "dev"]

# Production stage
FROM node:bullseye-slim AS prod

WORKDIR /app

# Copy only the built output and node_modules from the build stage
COPY --from=build /app /app

# Build the Next.js application
RUN npm run build

# Expose production port
EXPOSE 3000

# Run the production server
CMD ["npm", "run", "start"]


