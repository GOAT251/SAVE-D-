// Configuration de Face-API.js
const MODEL_URL = '/static/models';

// Options de détection
const detectionOptions = {
    // Utiliser un modèle plus léger pour de meilleures performances
    inputSize: 320,
    scoreThreshold: 0.5
};

// Initialisation de Face-API.js
async function initFaceAPI() {
    try {
        await faceapi.nets.tinyFaceDetector.loadFromUri(MODEL_URL);
        await faceapi.nets.faceLandmark68TinyNet.loadFromUri(MODEL_URL);
        await faceapi.nets.faceRecognitionNet.loadFromUri(MODEL_URL);
        console.log('Modèles chargés avec succès');
        return true;
    } catch (error) {
        console.error('Erreur lors du chargement des modèles:', error);
        return false;
    }
}

// Analyse du visage
async function analyzeFace(image) {
    try {
        const detection = await faceapi.detectSingleFace(
            image,
            new faceapi.TinyFaceDetectorOptions(detectionOptions)
        ).withFaceLandmarks(true);

        if (!detection) {
            throw new Error('Aucun visage détecté');
        }

        // Calculer les ratios faciaux
        const landmarks = detection.landmarks;
        const measurements = {
            // Ratio des tiers du visage
            upperThird: calculateUpperThird(landmarks),
            middleThird: calculateMiddleThird(landmarks),
            lowerThird: calculateLowerThird(landmarks),
            
            // Symétrie
            symmetryScore: calculateSymmetry(landmarks),
            
            // Autres mesures
            eyeDistance: calculateEyeDistance(landmarks),
            jawWidth: calculateJawWidth(landmarks)
        };

        return {
            detection,
            measurements
        };
    } catch (error) {
        console.error('Erreur lors de l\'analyse:', error);
        throw error;
    }
}

// Fonctions de calcul des mesures
function calculateUpperThird(landmarks) {
    const points = landmarks.positions;
    // Distance entre le haut du front et les sourcils
    return Math.abs(points[24].y - points[0].y);
}

function calculateMiddleThird(landmarks) {
    const points = landmarks.positions;
    // Distance entre les sourcils et le nez
    return Math.abs(points[30].y - points[24].y);
}

function calculateLowerThird(landmarks) {
    const points = landmarks.positions;
    // Distance entre le nez et le menton
    return Math.abs(points[8].y - points[30].y);
}

function calculateSymmetry(landmarks) {
    const points = landmarks.positions;
    let symmetryScore = 0;
    
    // Comparer les points des deux côtés du visage
    for (let i = 0; i < 16; i++) {
        const leftPoint = points[i];
        const rightPoint = points[16 - i];
        const distance = Math.abs(leftPoint.x - rightPoint.x);
        symmetryScore += distance;
    }
    
    return 100 - (symmetryScore / 16); // Score sur 100
}

function calculateEyeDistance(landmarks) {
    const points = landmarks.positions;
    // Distance entre les yeux
    return Math.abs(points[36].x - points[45].x);
}

function calculateJawWidth(landmarks) {
    const points = landmarks.positions;
    // Largeur de la mâchoire
    return Math.abs(points[2].x - points[14].x);
}

// Affichage des résultats
function displayResults(canvas, measurements) {
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Afficher les mesures sur le canvas
    ctx.font = '16px Arial';
    ctx.fillStyle = '#00ff00';
    
    let y = 30;
    for (const [key, value] of Object.entries(measurements)) {
        ctx.fillText(`${key}: ${Math.round(value)}`, 10, y);
        y += 25;
    }
}

// Export des fonctions
window.FaceAnalysis = {
    init: initFaceAPI,
    analyze: analyzeFace,
    displayResults: displayResults
}; 