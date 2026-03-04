                        backgroundColor: "rgba(0, 255, 65, 0.1)",
                        fill: true,
                        tension: 0.4
                    }]
                },
                options: { 
                    responsive: true,
                    scales: { y: { beginAtZero: false, grid: { color: "#1a1a1a" } } }
                }
            });
        }
    } catch (e) { console.error("Sync Error", e); }
}
setInterval(updateDashboard, 12000);
updateDashboard();
