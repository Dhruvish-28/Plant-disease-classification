'use client';

import { useState } from 'react';
import ImageUploadSection from '@/components/ImageUploadSection';
import ResultsDisplay from '@/components/ResultsDisplay';

export default function Home() {
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [uploadedImage, setUploadedImage] = useState<string | null>(null);

  const handleClassify = async (file: File) => {
    setLoading(true);
    setResults(null);

    // Preview the uploaded image
    const reader = new FileReader();
    reader.onloadend = () => {
      setUploadedImage(reader.result as string);
    };
    reader.readAsDataURL(file);

    try {
      // Create FormData for file upload
      const formData = new FormData();
      formData.append("file", file);

      // Call Flask backend
      const response = await fetch('https://dhruvish-28-plant-disease-classification.hf.space/classify', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Classification failed');
      }

      const data = await response.json();
      setResults(data.predictions);
    } catch (error) {
      setResults({
        error: error instanceof Error ? error.message : 'An error occurred',
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-background">
      <div className="container mx-auto px-4 py-12">
        {/* Header */}
        <header className="mb-12 text-center">
          <h1 className="mb-4 text-4xl font-bold text-primary md:text-5xl">
            Plant Disease Classifier
          </h1>
          <p className="text-lg text-muted-foreground">
            Upload an image of a plant leaf to identify diseases and get treatment recommendations
          </p>
        </header>

        {/* Main Content */}
        <div className="grid gap-8 md:grid-cols-2">
          {/* Left Column - Upload Section */}
          <ImageUploadSection onClassify={handleClassify} loading={loading} />

          {/* Right Column - Results Section */}
          <ResultsDisplay
            results={results}
            loading={loading}
            uploadedImage={uploadedImage}
          />
        </div>
      </div>
    </main>
  );
}
