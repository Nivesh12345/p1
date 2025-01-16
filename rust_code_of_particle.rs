use wasm_bindgen::prelude::*;
use js_sys::{Float64Array, Array, Math};

fn random_between(min: f64, max: f64) -> f64 {
    Math::random() * (max - min) + min
}

#[wasm_bindgen]
pub struct Particle {
    x: f64,
    y: f64,
    color: String,
    size: f64,
    sx: f64,
    sy: f64,
}

#[wasm_bindgen]
impl Particle {
    pub fn new(x: f64, y: f64, color: String) -> Particle {
        Particle {
            x,
            y,
            size: random_between(10.0, 15.0),
            sx: random_between(-3.0, 3.0),
            sy: random_between(-3.0, 3.0),
            color,
        }
    }

    pub fn update(&mut self) {
        self.x += self.sx;
        self.y += self.sy;
        if self.size > 0.2 {
            self.size -= 0.08;
        }
    }

    pub fn is_alive(&self) -> bool {
        self.size >= 0.3
    }

    pub fn get_data(&self) -> Array {
        let data = Array::new();
        data.push(&JsValue::from_f64(self.x));
        data.push(&JsValue::from_f64(self.y));
        data.push(&JsValue::from_f64(self.size));
        data.push(&JsValue::from(&self.color));
        data
    }
}

#[wasm_bindgen]
pub struct ParticleSystem {
    particles: Vec<Particle>,
}

#[wasm_bindgen]
impl ParticleSystem {
    #[wasm_bindgen(constructor)]
    pub fn new() -> ParticleSystem {
        ParticleSystem {
            particles: Vec::new(),
        }
    }

    pub fn add_particles(&mut self, x: f64, y: f64, color: String, count: usize) {
        for _ in 0..count {
            self.particles.push(Particle::new(x, y, color.clone()));
        }
    }

    pub fn update(&mut self) {
        for particle in self.particles.iter_mut() {
            particle.update();
        }
        self.particles.retain(|p| p.is_alive());
    }

    pub fn get_particle_data(&self) -> Array {
        let data = Array::new();
        for particle in &self.particles {
            data.push(&particle.get_data());
        }
        data
    }
}
