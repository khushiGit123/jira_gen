/** @type {import('next').NextConfig} */
const nextConfig = {
  async rewrites() {
    return [
      {
        source: '/api/python/:path*',
        destination: 'http://localhost:8000/:path*', // Python backend port
      },
    ]
  },
}

module.exports = nextConfig