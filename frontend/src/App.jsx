import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'

function App() {
  const lucknowPosition = [26.8467, 80.9462]

  return (
    <div style={{ width: '100vw', height: '100vh' }}>
      <MapContainer
        center={lucknowPosition}
        zoom={12}
        style={{ width: '100%', height: '100%' }}
      >
        <TileLayer
          attribution='&copy; OpenStreetMap contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        <Marker position={lucknowPosition}>
          <Popup>
            <strong>INFRA SHEILD</strong>
            <br />
            Lucknow Rainfall Reference Point
          </Popup>
        </Marker>
      </MapContainer>
    </div>
  )
}

export default App