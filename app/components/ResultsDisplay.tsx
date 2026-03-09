'use client';

import React from 'react';
import { AlertCircle, CheckCircle, Loader } from 'lucide-react';
import { Card } from '@/components/ui/card';

interface ResultsDisplayProps {
  results: any;
  loading: boolean;
  uploadedImage: string | null;
}

export default function ResultsDisplay({
  results,
  loading,
  uploadedImage,
}: ResultsDisplayProps) {
  return (
    <Card className="flex flex-col gap-6 border-2 border-border bg-card p-8">
      <div className="mb-2">
        <h2 className="text-2xl font-bold text-primary">Step 2: Results</h2>
        <p className="mt-1 text-sm text-muted-foreground">
          AI-powered disease classification
        </p>
      </div>

      {/* Image Preview */}
      {uploadedImage && (
        <div className="flex flex-col gap-2">
          <p className="text-sm font-semibold text-primary">Uploaded Image:</p>
          <div className="relative h-64 overflow-hidden rounded-lg border-2 border-border bg-secondary/30">
            <img
              src={uploadedImage}
              alt="Uploaded plant leaf"
              className="h-full w-full object-cover"
            />
          </div>
        </div>
      )}

      {/* Loading State */}
      {loading && (
        <div className="flex flex-col items-center justify-center gap-4 py-12">
          <Loader className="h-12 w-12 animate-spin text-accent" />
          <p className="text-lg font-semibold text-primary">
            Analyzing your plant image...
          </p>
          <p className="text-sm text-muted-foreground">
            This usually takes a few seconds
          </p>
        </div>
      )}

      {/* Initial State - No Results Yet */}
      {!loading && !results && !uploadedImage && (
        <div className="flex flex-col items-center justify-center gap-3 py-12">
          <div className="rounded-full bg-secondary/50 p-4">
            <AlertCircle className="h-8 w-8 text-muted-foreground" />
          </div>
          <p className="text-center text-lg font-semibold text-primary">
            Waiting for image upload
          </p>
          <p className="text-center text-sm text-muted-foreground">
            Upload an image to get started
          </p>
        </div>
      )}

      {/* Error State */}
      {!loading && results?.error && (
        <div className="flex flex-col gap-4 rounded-lg border-2 border-destructive/50 bg-destructive/10 p-6">
          <div className="flex items-center gap-2">
            <AlertCircle className="h-6 w-6 text-destructive" />
            <h3 className="font-semibold text-destructive">Classification Error</h3>
          </div>
          <p className="text-sm text-destructive">{results.error}</p>
        </div>
      )}

      {/* Success State */}
      {!loading && results && !results.error && (
        <div className="flex flex-col gap-6">
          {/* Classification Result */}
          <div className="rounded-lg border-2 border-accent/30 bg-accent/5 p-6">
            <div className="flex items-start gap-3">
              <CheckCircle className="mt-1 h-6 w-6 text-accent flex-shrink-0" />
              <div className="flex-1">
                <p className="text-sm font-semibold text-muted-foreground">
                  Detected Disease
                </p>
                <p className="mt-2 text-2xl font-bold text-primary">
                  {results.disease}
                </p>
              </div>
            </div>
          </div>

          {/* Confidence Score */}
          <div className="flex flex-col gap-3">
            <div className="flex items-center justify-between">
              <p className="text-sm font-semibold text-primary">Confidence Level</p>
              <p className="text-2xl font-bold text-accent">
                {results.confidence}%
              </p>
            </div>
            <div className="h-3 w-full overflow-hidden rounded-full bg-border">
              <div
                className="h-full bg-accent transition-all"
                style={{
                  width: `${Math.min(results.confidence, 100)}%`,
                }}
              />
            </div>
          </div>

          {/* All Predictions */}
          {results.all_predictions && (
            <div className="flex flex-col gap-3">
              <p className="text-sm font-semibold text-primary">All Predictions</p>
              <div className="space-y-2">
                {Object.entries(results.all_predictions)
                  .sort(([, a], [, b]) => (b as number) - (a as number))
                  .map(([disease, confidence]) => (
                    <div key={disease} className="flex items-center justify-between">
                      <p className="text-sm text-foreground">{disease}</p>
                      <div className="flex items-center gap-2">
                        <div className="h-2 w-24 overflow-hidden rounded-full bg-border">
                          <div
                            className="h-full bg-muted"
                            style={{
                              width: `${
                                Math.min(
                                  (confidence as number),
                                  100
                                )
                              }%`,
                            }}
                          />
                        </div>
                        <p className="w-12 text-right text-xs font-semibold text-muted-foreground">
                          {((confidence as number)).toFixed(1)}%
                        </p>
                      </div>
                    </div>
                  ))}
              </div>
            </div>
          )}
        </div>
      )}
    </Card>
  );
}
