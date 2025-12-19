# Overview

The Reborn is a browser-based multiplayer crime RPG game (tagline: "A nova era do crime começou"). Players create criminal characters, choose professions (Assassin, Drug Dealer, Pimp, Robber, etc.), and engage in various criminal activities including solo robberies, gang assaults, nightlife interactions, drug dealing, stock trading, and real-time PvP combat in designated zones called "raves."

The application is built as a full-stack TypeScript/React application with a Node.js/Express backend, real-time WebSocket communication via Socket.IO, and a retro-inspired dark UI reminiscent of classic crime web games.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture

**Technology Stack:**
- React 18 with TypeScript
- Vite as the build tool and dev server
- Wouter for client-side routing
- TanStack Query for server state management
- Tailwind CSS with custom dark theme (retro crime game aesthetic)
- shadcn/ui component library (New York style variant)
- Socket.IO client for real-time multiplayer features

**State Management:**
- Global game state managed via React Context (`GameProvider` in `client/src/lib/game-context.tsx`)
- Player stats stored in context include: intelligence, force, charisma, resistance, money, respect, stamina, addiction, tickets, bank money, credits, character class, username, avatar, profession level, drug inventory, drug transactions, hookers, factories, and mission progress
- Local storage used for persistence of active username and session data

**Component Structure:**
- Layout wrapper (`client/src/components/layout.tsx`) provides consistent sidebar navigation and player stats display
- Page-based routing with protected routes requiring authentication
- UI components from shadcn/ui in `client/src/components/ui/`

**Real-time Multiplayer:**
- Custom rave system (`client/src/lib/rave-system.ts`) manages WebSocket connections
- EventEmitter pattern for client-side event handling
- Real-time player synchronization in PvP zones (raves)

## Backend Architecture

**Technology Stack:**
- Node.js with Express framework
- TypeScript throughout
- Socket.IO for WebSocket server
- In-memory storage (MemStorage class) for user data
- HTTP server created with Node's `http` module to support both Express and Socket.IO

**Server Structure:**
- Entry point: `server/index.ts`
- Routes defined in `server/routes.ts`
- Static file serving via `server/static.ts`
- Vite dev server integration in development (`server/vite.ts`)
- Storage abstraction via `IStorage` interface in `server/storage.ts`

**WebSocket Server (Multiplayer):**
- Socket.IO server attached to HTTP server
- Manages real-time rave system with player tracking
- Server is authoritative for: player positions, combat resolution, timers, player lists
- Active players stored in Map structure with socket IDs as keys
- 8-second timer system for rave participation
- Combat damage calculation based on assault power differentials

**API Design:**
- RESTful endpoints would be defined in `server/routes.ts`
- Currently implements WebSocket-based multiplayer only
- Session management prepared but not fully implemented

## Data Storage

**Database:**
- Drizzle ORM configured for PostgreSQL (via `drizzle.config.ts`)
- Neon serverless PostgreSQL as the database provider
- Schema defined in `shared/schema.ts`
- Current schema includes: users table, friendships table
- Database migrations stored in `./migrations` directory

**Schema Entities:**
- **Users**: id (UUID), username (unique), password
- **Friendships**: id (UUID), requester_id, addressee_id, status (pending/accepted)

**Current State:**
- In-memory storage (`MemStorage`) used for development/prototyping
- Database schema prepared but application logic uses memory storage
- Production deployment would require switching from MemStorage to database-backed storage

## External Dependencies

**Third-Party Services:**
- Neon Database (serverless PostgreSQL hosting)
- Replit deployment platform (configured via vite plugins)

**Key NPM Packages:**
- **UI/Frontend**: @radix-ui/* components, @tanstack/react-query, react-hook-form, zod validation, framer-motion, date-fns
- **Backend**: express, socket.io, drizzle-orm, drizzle-zod, connect-pg-simple (session store)
- **Build Tools**: vite, esbuild, tsx, tailwindcss, autoprefixer
- **WebSocket**: socket.io (client and server), ws
- **Development**: @replit/vite-plugin-* (dev banner, cartographer, runtime error modal)

**Asset Management:**
- Static assets stored in `client/public/` and `attached_assets/`
- Generated images for game UI elements
- Stock photos for robbery scenarios
- Custom weapon icons

**Authentication:**
- Prepared but not fully implemented
- Admin panel has hardcoded credentials (teste123/Spired2@@)
- User authentication logic exists in storage layer but not connected to routes

**Custom Vite Plugins:**
- `vite-plugin-meta-images.ts`: Updates OpenGraph/Twitter meta tags with Replit deployment URL
- Replit-specific plugins for development experience and deployment